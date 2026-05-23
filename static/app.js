// App.js - Client-side functionality

document.addEventListener('DOMContentLoaded', () => {
    // Toast Notification System
    window.showToast = (message, type = 'success') => {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const toast = document.createElement('div');
        const bgColor = type === 'success' ? 'bg-green-500' : (type === 'error' ? 'bg-red-500' : 'bg-blue-500');
        
        toast.className = `${bgColor} text-white px-4 py-3 rounded shadow-lg flex items-center font-code text-sm toast-enter`;
        
        const icon = type === 'success' 
            ? `<svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>`
            : `<svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`;

        toast.innerHTML = `
            ${icon}
            <span>${message}</span>
        `;

        container.appendChild(toast);

        // Remove toast after 3 seconds
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            toast.style.transition = 'all 0.3s ease-out';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    };

    // Form submission loading state
    const analyzeForm = document.getElementById('analyze-form');
    if (analyzeForm) {
        analyzeForm.addEventListener('submit', (e) => {
            const btn = document.getElementById('analyze-btn');
            const btnText = document.getElementById('btn-text');
            const btnIcon = document.getElementById('btn-icon');
            const btnSpinner = document.getElementById('btn-spinner');

            if (btn && btnText && btnSpinner) {
                // Disable button and show spinner
                btn.disabled = true;
                btn.classList.add('opacity-75', 'cursor-not-allowed');
                btnText.textContent = 'Analyzing...';
                if (btnIcon) btnIcon.classList.add('hidden');
                btnSpinner.classList.remove('hidden');

                showToast('Analysis started. This may take a moment...', 'info');
            }
        });
    }

    // Welcome toast
    if (window.location.pathname === '/' || window.location.pathname === '/analyze/') {
        setTimeout(() => {
            showToast('Welcome to CodePilot AI!', 'success');
        }, 500);
    }
});
