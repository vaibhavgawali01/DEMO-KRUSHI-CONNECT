/**
 * 🌱 Krushi Seva Kendra - Core Application JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Dark Mode Management
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const currentTheme = localStorage.getItem('krushi_theme') || 'light';

    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        updateThemeIcon(true);
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('krushi_theme', 'light');
                updateThemeIcon(false);
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('krushi_theme', 'dark');
                updateThemeIcon(true);
            }
        });
    }

    function updateThemeIcon(isDark) {
        if (!themeToggleBtn) return;
        themeToggleBtn.innerHTML = isDark 
            ? '<i class="bi bi-sun-fill text-warning"></i>' 
            : '<i class="bi bi-moon-stars-fill"></i>';
    }

    // 2. Global Live Product Search with Autocomplete
    const globalSearchInput = document.getElementById('globalSearchInput');
    const searchDropdown = document.getElementById('searchDropdownResults');

    if (globalSearchInput && searchDropdown) {
        let debounceTimer;
        globalSearchInput.addEventListener('input', (e) => {
            const query = e.target.value.trim();
            clearTimeout(debounceTimer);

            if (query.length < 2) {
                searchDropdown.style.display = 'none';
                searchDropdown.innerHTML = '';
                return;
            }

            debounceTimer = setTimeout(() => {
                fetch(`/api/products/search?q=${encodeURIComponent(query)}`)
                    .then(res => res.json())
                    .then(res => {
                        if (res.success && res.data.length > 0) {
                            let html = '<div class="list-group list-group-flush">';
                            res.data.forEach(prod => {
                                html += `
                                    <a href="/products/${prod.id}" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between py-2">
                                        <div>
                                            <strong class="text-success">${escapeHtml(prod.name)}</strong>
                                            <div class="small text-muted">${escapeHtml(prod.company)} | ${escapeHtml(prod.category.name)}</div>
                                        </div>
                                        <span class="badge bg-success rounded-pill">₹${prod.effectivePrice}</span>
                                    </a>
                                `;
                            });
                            html += '</div>';
                            searchDropdown.innerHTML = html;
                            searchDropdown.style.display = 'block';
                        } else {
                            searchDropdown.innerHTML = '<div class="p-3 text-center text-muted small">No products found / उत्पादन सापडले नाही</div>';
                            searchDropdown.style.display = 'block';
                        }
                    })
                    .catch(err => console.error('Search error:', err));
            }, 250);
        });

        // Hide search dropdown on click outside
        document.addEventListener('click', (e) => {
            if (!globalSearchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
                searchDropdown.style.display = 'none';
            }
        });
    }

    // 3. Dynamic UPI QR Code Modal Generator
    window.openUpiModal = function(amount, note, upiId) {
        const modalEl = document.getElementById('upiQrModal');
        if (!modalEl) return;

        const amtFormatted = parseFloat(amount || 0).toFixed(2);
        const upiPayUrl = `upi://pay?pa=${encodeURIComponent(upiId || 'krushiseva@okaxis')}&pn=Krushi+Seva+Kendra&am=${amtFormatted}&cu=INR&tn=${encodeURIComponent(note || 'Krushi Payment')}`;
        
        // Generate QR code using public dynamic QR API
        const qrImageEl = document.getElementById('upiQrImage');
        const amountDisplay = document.getElementById('upiModalAmount');
        const qrApiUrl = `https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=${encodeURIComponent(upiPayUrl)}`;

        if (qrImageEl) qrImageEl.src = qrApiUrl;
        if (amountDisplay) amountDisplay.innerText = `₹${amtFormatted}`;

        const modal = new bootstrap.Modal(modalEl);
        modal.show();
    };

    // 4. Helper for HTML escaping
    function escapeHtml(text) {
        if (!text) return '';
        const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
        return text.toString().replace(/[&<>"']/g, m => map[m]);
    }
});
