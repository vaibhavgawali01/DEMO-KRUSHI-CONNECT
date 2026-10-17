/**
 * 🌱 Krushi Seva Kendra - Admin Management Scripts & Analytics
 */

document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.admin-sidebar-wrap')) {
        initBarcodeScanner();
    }
});

function initBarcodeScanner() {
    let barcodeBuffer = '';
    let lastKeyTime = Date.now();

    document.addEventListener('keydown', (e) => {
        const currentTime = Date.now();
        // Hardware scanners typically type characters < 30ms apart
        if (currentTime - lastKeyTime > 100) {
            barcodeBuffer = '';
        }
        lastKeyTime = currentTime;

        if (e.key === 'Enter' && barcodeBuffer.length >= 6) {
            // Scanner finished emitting barcode
            console.log('Barcode scanned:', barcodeBuffer);
            lookupProductByBarcode(barcodeBuffer);
            barcodeBuffer = '';
        } else if (e.key.length === 1) {
            barcodeBuffer += e.key;
        }
    });
}

function lookupProductByBarcode(barcode) {
    fetch(`/api/products/barcode/${encodeURIComponent(barcode)}`)
        .then(res => res.json())
        .then(res => {
            if (res.success && res.data) {
                const prod = res.data;
                alert(`Product Found via Barcode Scan:\nName: ${prod.name}\nPrice: ₹${prod.price}\nCurrent Stock: ${prod.stockQuantity}`);
                window.location.href = `/admin/products/${prod.id}/edit`;
            } else {
                alert(`No product found for scanned barcode: ${barcode}`);
            }
        })
        .catch(err => console.error('Barcode lookup failed:', err));
}

// Helper to open Stock Adjustment Modal
window.openStockModal = function(productId, productName, currentStock) {
    const modalEl = document.getElementById('stockAdjustmentModal');
    if (!modalEl) return;

    document.getElementById('modalProductId').value = productId;
    document.getElementById('modalProductName').innerText = productName;
    document.getElementById('modalCurrentStock').innerText = currentStock;
    document.getElementById('stockForm').action = `/admin/products/${productId}/adjust-stock`;

    const modal = new bootstrap.Modal(modalEl);
    modal.show();
};

// Helper to open Udhari Payment Modal
window.openUdhariPayModal = function(udhariId, customerName, remainingAmount) {
    const modalEl = document.getElementById('recordUdhariPaymentModal');
    if (!modalEl) return;

    document.getElementById('udhariPayModalId').value = udhariId;
    document.getElementById('udhariPayCustomerName').innerText = customerName;
    document.getElementById('udhariPayRemaining').innerText = '₹' + remainingAmount;
    document.getElementById('udhariPayAmountInput').value = remainingAmount;
    document.getElementById('udhariPayAmountInput').max = remainingAmount;

    const modal = new bootstrap.Modal(modalEl);
    modal.show();
};

// Helper to open Udhari Reminder Modal
window.openReminderModal = function(userId, udhariId, customerName, mobile, amount, dueDate, isOverdue) {
    const modalEl = document.getElementById('sendReminderModal');
    if (!modalEl) return;

    document.getElementById('reminderUserId').value = userId;
    document.getElementById('reminderUdhariId').value = udhariId || '';
    document.getElementById('reminderCustomerName').innerText = customerName;
    document.getElementById('reminderMobile').innerText = mobile;

    const messageTextarea = document.getElementById('reminderMessageText');
    if (isOverdue) {
        messageTextarea.value = `Dear ${customerName}, your Udhari payment of ₹${amount} was due on ${dueDate} and is now overdue. Kindly make the payment at the earliest. - Krushi Seva Kendra`;
    } else {
        messageTextarea.value = `Dear ${customerName}, your outstanding Udhari balance is ₹${amount}. Please pay before ${dueDate}. Thank you! - Krushi Seva Kendra`;
    }

    const modal = new bootstrap.Modal(modalEl);
    modal.show();
};

// Helper to open Add Credit Customer Modal
window.openCreateUdhariModal = function() {
    const modalEl = document.getElementById('createUdhariModal');
    if (!modalEl) return;
    try {
        if (typeof bootstrap !== 'undefined' && bootstrap.Modal) {
            const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
            modal.show();
            return;
        }
    } catch(e) {}
    modalEl.classList.add('show');
    modalEl.style.display = 'block';
    document.body.classList.add('modal-open');
};
