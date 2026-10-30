/**
 * 🌱 Krushi Seva Kendra - Smart Farming Advisory Scripts
 */

document.addEventListener('DOMContentLoaded', () => {
    const calcCropSelect = document.getElementById('calcCrop');
    const calcAreaInput = document.getElementById('calcArea');
    const calcSoilSelect = document.getElementById('calcSoil');
    const calcStageSelect = document.getElementById('calcStage');

    if (calcCropSelect && calcAreaInput) {
        const updateCalc = () => {
            const crop = calcCropSelect.value;
            const area = parseFloat(calcAreaInput.value || 1);
            const soil = calcSoilSelect ? calcSoilSelect.value : 'Medium Black';
            const stage = calcStageSelect ? calcStageSelect.value : 'Full Season';

            fetch(`/api/farming/fertilizer-calc?crop=${encodeURIComponent(crop)}&acres=${area}&soilType=${encodeURIComponent(soil)}&stage=${encodeURIComponent(stage)}`)
                .then(res => res.json())
                .then(res => {
                    if (res.success && res.data) {
                        const data = res.data;
                        const reqNEl = document.getElementById('calcResN');
                        const reqPEl = document.getElementById('calcResP');
                        const reqKEl = document.getElementById('calcResK');
                        const ureaBagsEl = document.getElementById('calcUreaBags');
                        const sspBagsEl = document.getElementById('calcSspBags');
                        const mopBagsEl = document.getElementById('calcMopBags');
                        const complexNameEl = document.getElementById('calcComplexName');
                        const complexBagsEl = document.getElementById('calcComplexBags');
                        const costEl = document.getElementById('calcEstCost');

                        if (reqNEl) reqNEl.innerText = data.requiredN + ' kg';
                        if (reqPEl) reqPEl.innerText = data.requiredP + ' kg';
                        if (reqKEl) reqKEl.innerText = data.requiredK + ' kg';
                        if (ureaBagsEl) ureaBagsEl.innerText = data.ureaBags + ' Bags (45kg)';
                        if (sspBagsEl) sspBagsEl.innerText = data.sspBags + ' Bags (50kg)';
                        if (mopBagsEl) mopBagsEl.innerText = data.mopBags + ' Bags (50kg)';
                        if (complexNameEl) complexNameEl.innerText = data.complexFertilizerName;
                        if (complexBagsEl) complexBagsEl.innerText = data.complexBags + ' Bags + ' + data.supplementaryUreaBags + ' Bags Urea';
                        if (costEl) costEl.innerText = '₹' + data.estimatedTotalCost;
                    }
                })
                .catch(err => console.error('Fertilizer calc error:', err));
        };

        calcCropSelect.addEventListener('change', updateCalc);
        calcAreaInput.addEventListener('input', updateCalc);
        if (calcSoilSelect) calcSoilSelect.addEventListener('change', updateCalc);
        if (calcStageSelect) calcStageSelect.addEventListener('change', updateCalc);
    }
});
