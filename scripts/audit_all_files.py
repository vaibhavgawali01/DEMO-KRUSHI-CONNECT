import os
import re
from html.parser import HTMLParser

dist_dir = 'dist'
html_files = []
for root, dirs, files in os.walk(dist_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Total HTML files found: {len(html_files)}")

class AuditParser(HTMLParser):
    def __init__(self, filename, content):
        super().__init__()
        self.filename = filename
        self.content = content
        self.buttons = []
        self.links = []
        self.images = []
        self.in_form = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == 'form':
            self.in_form = True
        elif tag == 'button':
            self.buttons.append((attr_dict, self.in_form))
        elif tag == 'a':
            self.links.append(attr_dict)
        elif tag == 'img':
            self.images.append(attr_dict)

    def handle_endtag(self, tag):
        if tag == 'form':
            self.in_form = False

dead_buttons = []
broken_links = []
missing_images = []

for h in html_files:
    rel_path = os.path.relpath(h, dist_dir).replace('\\', '/')
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()

    parser = AuditParser(rel_path, content)
    parser.feed(content)

    # 1. Check buttons
    for attrs, in_form in parser.buttons:
        btn_type = attrs.get('type', '').lower()
        onclick = attrs.get('onclick', '').strip()
        data_toggle = attrs.get('data-bs-toggle') or attrs.get('data-toggle')
        data_dismiss = attrs.get('data-bs-dismiss') or attrs.get('data-dismiss')
        btn_id = attrs.get('id', '')
        btn_class = attrs.get('class', '')

        has_behavior = False
        if onclick:
            has_behavior = True
        elif btn_type == 'submit' and in_form:
            has_behavior = True
        elif data_toggle or data_dismiss:
            has_behavior = True
        elif btn_id and (f"getElementById('{btn_id}')" in content or f'getElementById("{btn_id}")' in content or f"#{btn_id}" in content):
            has_behavior = True
        elif 'btn-close' in btn_class and (data_dismiss or onclick):
            has_behavior = True
        elif 'navbar-toggler' in btn_class:
            has_behavior = True
        elif any(cls in content and ('addEventListener' in content or '$(' in content) for cls in btn_class.split()):
            has_behavior = True

        if not has_behavior:
            dead_buttons.append({
                'file': rel_path,
                'id': btn_id,
                'class': btn_class,
                'type': btn_type,
                'in_form': in_form
            })

    # 2. Check links
    for attrs in parser.links:
        href = attrs.get('href', '').strip()
        onclick = attrs.get('onclick', '').strip()
        a_id = attrs.get('id', '')
        a_class = attrs.get('class', '')
        data_toggle = attrs.get('data-bs-toggle') or attrs.get('data-bs-dismiss')

        if not href or href == '#' or href.startswith('javascript:'):
            has_click = bool(onclick) or (a_id and (f"getElementById('{a_id}')" in content or f'getElementById("{a_id}")' in content))
            if not has_click and not data_toggle and 'dropdown-toggle' not in a_class:
                broken_links.append({
                    'file': rel_path,
                    'href': href,
                    'class': a_class,
                    'id': a_id
                })
        elif not href.startswith('http') and not href.startswith('tel:') and not href.startswith('mailto:') and not href.startswith('sms:') and not href.startswith('#'):
            clean_href = href.split('?')[0].split('#')[0]
            if clean_href.endswith('.html'):
                file_dir = os.path.dirname(h)
                target1 = os.path.join(file_dir, clean_href)
                target2 = os.path.join(dist_dir, clean_href)
                if not os.path.exists(target1) and not os.path.exists(target2):
                    broken_links.append({
                        'file': rel_path,
                        'href': href,
                        'class': a_class,
                        'id': a_id
                    })

    # 3. Check images
    for attrs in parser.images:
        src = attrs.get('src', '').strip()
        if src and not src.startswith('http') and not src.startswith('data:') and not '${' in src:
            clean_src = src.split('?')[0].split('#')[0]
            if clean_src.startswith('/'):
                target1 = os.path.join(dist_dir, clean_src.lstrip('/'))
            else:
                target1 = os.path.join(os.path.dirname(h), clean_src)
            target2 = os.path.join(dist_dir, clean_src)
            if not os.path.exists(target1) and not os.path.exists(target2):
                missing_images.append({
                    'file': rel_path,
                    'src': src
                })

print(f"\n--- AUDIT RESULTS ---")
print(f"Potentially unhandled buttons: {len(dead_buttons)}")
for b in dead_buttons[:15]:
    print(f"  [{b['file']}] id='{b['id']}' class='{b['class']}' type='{b['type']}' in_form={b['in_form']}")
if len(dead_buttons) > 15:
    print(f"  ... and {len(dead_buttons) - 15} more")

print(f"\nBroken or empty links: {len(broken_links)}")
for l in broken_links[:15]:
    print(f"  [{l['file']}] href='{l['href']}' class='{l['class']}' id='{l['id']}'")
if len(broken_links) > 15:
    print(f"  ... and {len(broken_links) - 15} more")

print(f"\nMissing images: {len(missing_images)}")
for m in missing_images[:15]:
    print(f"  [{m['file']}] src='{m['src']}'")
if len(missing_images) > 15:
    print(f"  ... and {len(missing_images) - 15} more")
