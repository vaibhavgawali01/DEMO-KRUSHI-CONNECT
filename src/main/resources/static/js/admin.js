/**
 * 🌱 Krushi Seva Kendra - Admin Management Scripts & Analytics
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Dashboard Charts (if elements present)
    initSalesChart();
    initPaymentMethodChart();

    // 2. Barcode Hardware Scanner Integration
    initBarcodeScanner();
});

function initSalesChart() {
    const ctx = document.getElementById('salesTrendChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Day 1', 'Day 5', 'Day 10', 'Day 15', 'Day 20', 'Day 25', 'Today'],
            datasets: [{
                label: 'Sales Revenue (₹)',
                data: [12500, 18200, 24600, 19400, 31000, 28500, 38900],
                borderColor: '#2e7d32',
                backgroundColor: 'rgba(46, 125, 50, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.35,
                pointBackgroundColor: '#1b5e20',
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) { return '₹' + value.toLocaleString(); }
                    }
                }
            }
        }
    });
}

function initPaymentMethodChart() {
    const ctx = document.getElementById('paymentMethodChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Cash', 'UPI / QR', 'Udhari (Credit)', 'Bank Transfer'],
            datasets: [{
                data: [45, 30, 20, 5],
                backgroundColor: ['#4caf50', '#2196f3', '#ff9800', '#9c27b0'],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
}

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
