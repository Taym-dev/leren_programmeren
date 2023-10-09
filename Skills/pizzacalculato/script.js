document.addEventListener("DOMContentLoaded", function () {
    const calculateButton = document.getElementById("calculate");
    const smallInput = document.getElementById("small");
    const mediumInput = document.getElementById("medium");
    const largeInput = document.getElementById("large");
    const resultDiv = document.getElementById("result");
    const smallOrder = document.getElementById("small-order");
    const mediumOrder = document.getElementById("medium-order");
    const largeOrder = document.getElementById("large-order");
    const totalOrder = document.getElementById("total-order");
    const currentYear = document.getElementById("current-year");

    calculateButton.addEventListener("click", function () {
        const smallCount = parseInt(smallInput.value) || 0;
        const mediumCount = parseInt(mediumInput.value) || 0;
        const largeCount = parseInt(largeInput.value) || 0;
        const smallPrice = 5; // Prijs voor small pizza
        const mediumPrice = 8; // Prijs voor medium pizza
        const largePrice = 10; // Prijs voor large pizza

        // Bereken de totaalprijs per soort pizza
        const smallTotal = smallCount * smallPrice;
        const mediumTotal = mediumCount * mediumPrice;
        const largeTotal = largeCount * largePrice;
        const total = smallTotal + mediumTotal + largeTotal;

        // Toon de bestellingsoverzichten
        smallOrder.textContent = `Aantal Small Pizza's: ${smallCount}, Totaalprijs: €${smallTotal}`;
        mediumOrder.textContent = `Aantal Medium Pizza's: ${mediumCount}, Totaalprijs: €${mediumTotal}`;
        largeOrder.textContent = `Aantal Large Pizza's: ${largeCount}, Totaalprijs: €${largeTotal}`;
        totalOrder.textContent = `Totaalprijs: €${total}`;

        // Toon het resultaat
        resultDiv.style.display = "block";
    });

    // Vul het huidige jaar in de footer
    currentYear.textContent = new Date().getFullYear();
});
