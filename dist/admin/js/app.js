/**
 * 🌱 Krushi Seva Kendra - Core Application JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
    // Keep theme state in sync with the theme applied by premium.js.
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const currentTheme = localStorage.getItem('krushi-theme') || 'light';

    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
    } else {
        document.documentElement.removeAttribute('data-theme');
    }

    if (themeToggleBtn) {
        const icon = themeToggleBtn.querySelector('i');
        if (icon) {
            icon.className = currentTheme === 'dark'
                ? 'bi bi-sun-fill text-warning'
                : 'bi bi-moon-stars-fill';
        }
    }

    const globalSearchInput = document.getElementById('globalSearchInput');
    const searchDropdown = document.getElementById('searchDropdownResults');

    if (globalSearchInput && searchDropdown) {
        let debounceTimer;
        let requestSequence = 0;
        const closeSearchDropdown = () => {
            clearTimeout(debounceTimer);
            requestSequence++;
            searchDropdown.style.display = 'none';
            globalSearchInput.setAttribute('aria-expanded', 'false');
            searchDropdown.setAttribute('aria-busy', 'false');
        };
        const showSearchDropdown = () => {
            searchDropdown.style.display = 'block';
            globalSearchInput.setAttribute('aria-expanded', 'true');
        };

        globalSearchInput.addEventListener('input', () => {
            const query = globalSearchInput.value.trim();
            clearTimeout(debounceTimer);
            const currentRequest = ++requestSequence;

            if (query.length < 2) {
                searchDropdown.innerHTML = '';
                closeSearchDropdown();
                return;
            }

            searchDropdown.textContent = searchDropdown.dataset.loadingText || 'Searching products...';
            searchDropdown.setAttribute('aria-busy', 'true');
            showSearchDropdown();
            debounceTimer = setTimeout(() => {
                fetch(`/api/products/search?q=${encodeURIComponent(query)}`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`Search request failed with status ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(response => {
                        if (currentRequest !== requestSequence) return;
                        const products = response && response.success && Array.isArray(response.data)
                            ? response.data
                            : [];
                        if (products.length === 0) {
                            searchDropdown.innerHTML = '<div class="p-3 text-center text-muted small">No products found / उत्पादन सापडले नाही</div>';
                            searchDropdown.setAttribute('aria-busy', 'false');
                            showSearchDropdown();
                            return;
                        }

                        const html = products.map(product => {
                            const id = Number(product.id);
                            if (!Number.isSafeInteger(id) || id <= 0) return '';
                            const categoryName = product.category && product.category.name
                                ? product.category.name
                                : '';
                            return `
                                <a href="/products/${id}" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between py-2">
                                    <div>
                                        <strong class="text-success">${escapeHtml(product.name)}</strong>
                                        <div class="small text-muted">${escapeHtml(product.company)}${categoryName ? ` | ${escapeHtml(categoryName)}` : ''}</div>
                                    </div>
                                    <span class="badge bg-success rounded-pill">₹${escapeHtml(product.effectivePrice)}</span>
                                </a>
                            `;
                        }).join('');
                        searchDropdown.innerHTML = `<div class="list-group list-group-flush">${html}</div>`;
                        searchDropdown.setAttribute('aria-busy', 'false');
                        showSearchDropdown();
                    })
                    .catch(err => {
                        if (currentRequest !== requestSequence) return;
                        console.error('Search error:', err);
                        searchDropdown.innerHTML = '<div class="p-3 text-center text-muted small">Search is temporarily unavailable.</div>';
                        searchDropdown.setAttribute('aria-busy', 'false');
                        showSearchDropdown();
                    });
            }, 250);
        });

        globalSearchInput.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && searchDropdown.style.display !== 'none') {
                closeSearchDropdown();
                globalSearchInput.focus();
            }
        });

        document.addEventListener('click', (e) => {
            if (!globalSearchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
                closeSearchDropdown();
            }
        });
    }

    window.openUpiModal = function(amount, note, upiId) {
        const modalEl = document.getElementById('upiQrModal');
        if (!modalEl || !upiId) return;

        const parsedAmount = Number.parseFloat(amount);
        if (!Number.isFinite(parsedAmount) || parsedAmount <= 0) return;
        const amtFormatted = parsedAmount.toFixed(2);
        const upiPayUrl = `upi://pay?pa=${encodeURIComponent(upiId)}&pn=Krushi+Seva+Kendra&am=${amtFormatted}&cu=INR&tn=${encodeURIComponent(note || 'Krushi Payment')}`;
        const qrImageEl = document.getElementById('upiQrImage');
        const amountDisplay = document.getElementById('upiModalAmount');
        const upiIdDisplay = document.getElementById('upiModalId');
        const qrApiUrl = `https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=${encodeURIComponent(upiPayUrl)}`;

        if (qrImageEl) qrImageEl.src = qrApiUrl;
        if (amountDisplay) amountDisplay.innerText = `₹${amtFormatted}`;
        if (upiIdDisplay) upiIdDisplay.textContent = upiId;

        const modal = new bootstrap.Modal(modalEl);
        modal.show();
    };

    document.querySelectorAll('.upi-qr-trigger').forEach(button => {
        button.addEventListener('click', () => {
            window.openUpiModal(button.dataset.amount, 'Order Payment', button.dataset.upiId);
        });
    });

    function escapeHtml(text) {
        if (!text) return '';
        const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
        return text.toString().replace(/[&<>"']/g, m => map[m]);
    }
});
