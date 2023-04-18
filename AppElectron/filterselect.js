function setupMultiselect(multiselectId) {
    const multiselectWrapper = document.getElementById(multiselectId);
    const multiselectDisplay = multiselectWrapper.querySelector('.multiselect-display');
    const multiselectOptions = multiselectWrapper.querySelector('.multiselect-options');
    const checkboxes = multiselectWrapper.querySelectorAll('.multiselect-options input[type="checkbox"]');

    multiselectDisplay.addEventListener('click', function () {
        multiselectOptions.style.display = multiselectOptions.style.display === 'block' ? 'none' : 'block';
    });

    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            const selectedOptions = Array.from(multiselectWrapper.querySelectorAll('.multiselect-options input[type="checkbox"]:checked')).map(function (checkbox) {
                return checkbox.value;
            });
            multiselectDisplay.textContent = selectedOptions.length > 0 ? selectedOptions.join(', ') : 'Select '+multiselectWrapper.getAttribute('name');
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    setupMultiselect('multiselect-subject');
    setupMultiselect('multiselect-device');
});

function getSelectedOptions(multiselectId) {
    return Array.from(document.querySelectorAll(`#${multiselectId} .multiselect-options input[type="checkbox"]:checked`)).map(checkbox => checkbox.value);
}

function getSelectedDateRange() {
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    return {
        start_date: startDate,
        end_date: endDate
    };
}

async function submitData() {
    const selectedOptions1 = getSelectedOptions('multiselect-subject');
    const selectedOptions2 = getSelectedOptions('multiselect-device');
    const dateRange = getSelectedDateRange();

    const data = {
        multiselect_1: selectedOptions1,
        multiselect_2: selectedOptions2,
        ...dateRange
    };

    const response = await makeApiCall(data);
    sessionStorage.setItem('response',JSON.stringify(response));
    window.location.href = 'displays.html';
}

document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submit-btn');
    submitButton.addEventListener('click', submitData);
});

async function makeApiCall(data){
    try {
        const response = await fetch('/api/submit/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Include any additional headers required by your Django API (e.g., CSRF token, authentication token, etc.)
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            console.log('API response:', result);
        } else {
            console.error('API error:', response.statusText);
        }
    } catch (error) {
        console.error('API request failed:', error);
    }
    return result;
}
