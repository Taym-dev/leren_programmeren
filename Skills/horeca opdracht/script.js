const prijzen = {
    'fris': 2.50,
    'bier': 3.00,
    'wijn': 4.00,
    'frikandel': 2.00,
    'bitterballen_8': 5.00,
    'bitterballen_16': 9.00,
    'pizza': 8.00,
};

const bestellingen = {
    'drankjes': {},
    'snacks': {}
};

function voegBestellingToe() {
    const bestellingInput = document.getElementById('bestelling');
    const bestelling = bestellingInput.value.toLowerCase(); // Zet de invoer naar kleine letters om hoofdlettergevoelige problemen te voorkomen.

    if (bestelling === 'stop') {
        toonRekening();
        return;
    }

    if (bestelling in prijzen) {
        if (bestelling === 'snack') {
            voegSnackToe();
        } else {
            const aantal = parseInt(prompt(`Hoeveel ${bestelling} wilt u toevoegen aan uw bestelling?`));
            if (!isNaN(aantal)) {
                if (bestelling in bestellingen['drankjes']) {
                    bestellingen['drankjes'][bestelling] += aantal;
                } else {
                    bestellingen['drankjes'][bestelling] = aantal;
                }
                toonRekening();
            } else {
                alert('Ongeldige invoer. Voer een geldig aantal in.');
            }
        }
    } else {
        alert('Sorry, dat hebben we niet. Probeer opnieuw.');
    }

    bestellingInput.value = '';
}



function voegBestellingToe() {
    const bestellingInput = document.getElementById('bestelling');
    const bestelling = bestellingInput.value.trim().toLowerCase();

    if (bestelling === 'stop') {
        toonRekening();
        return; // Voeg een return toe om de functie te verlaten wanneer "stop" wordt ingevoerd.
    }

    if (bestelling in prijzen) {
        const isSnack = ['frikandel', 'bitterballen', 'pizza'].includes(bestelling);
        if (isSnack) {
            voegSnackToe(bestelling);
        } else {
            const aantal = parseInt(prompt(`Hoeveel ${bestelling} wilt u toevoegen aan uw bestelling?`));
            if (!isNaN(aantal)) {
                if (bestelling in bestellingen['drankjes']) {
                    bestellingen['drankjes'][bestelling] += aantal;
                } else {
                    bestellingen['drankjes'][bestelling] = aantal;
                }
                toonRekening();
            } else {
                alert('Ongeldige invoer. Voer een geldig aantal in.');
            }
        }
    } else {
        alert('Sorry, dat hebben we niet. Probeer opnieuw.');
    }

    bestellingInput.value = '';
}



function toonRekening() {
    const rekeningLijst = document.getElementById('rekening-lijst');
    rekeningLijst.innerHTML = '';
    let totaalbedrag = 0;

    for (const categorie in bestellingen) {
        for (const item in bestellingen[categorie]) {
            const aantal = bestellingen[categorie][item];
            const prijs = prijzen[item];
            const kosten = aantal * prijs;
            totaalbedrag += kosten;

            const li = document.createElement('li');
            li.innerText = `${item}: ${aantal} x €${prijs.toFixed(2)} = €${kosten.toFixed(2)}`;
            rekeningLijst.appendChild(li);
        }
    }

    const totaalbedragElement = document.getElementById('totaalbedrag');
    totaalbedragElement.innerText = `Totaal: €${totaalbedrag.toFixed(2)}`;
}

function wisBerekening() {
    // Wis de weergegeven rekening en het totaalbedrag
    const rekeningLijst = document.getElementById('rekening-lijst');
    rekeningLijst.innerHTML = '';
    const totaalbedragElement = document.getElementById('totaalbedrag');
    totaalbedragElement.innerText = '';
}

function restartBerekening() {
    // Reset alle bestellingen naar een lege staat
    bestellingen = {
        drankjes: {}
    };

    // Wis het bestelling-inputveld
    const bestellingInput = document.getElementById('bestelling');
    bestellingInput.value = '';

    // Wis de weergegeven berekening
    wisBerekening();
}


