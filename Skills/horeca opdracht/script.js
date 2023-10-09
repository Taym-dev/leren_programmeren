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




function voegSnackToe() {
    const snack = prompt('Welke snack wilt u bestellen? (frikandel/bitterballen/pizza)').toLowerCase();

    if (snack === 'bitterballen') {
        const aantalSchaal = parseInt(prompt('Hoeveel bitterballenschaal wilt u bestellen? (8 of 16)'));
        if (aantalSchaal === 8 || aantalSchaal === 16) {
            const aantalSchalen = parseInt(prompt(`Hoeveel bitterbalschalen van ${aantalSchaal} stuks wilt u bestellen?`));
            if (!isNaN(aantalSchalen)) {
                const item = `bitterballen_${aantalSchaal}`;
                if (item in bestellingen['snacks']) {
                    bestellingen['snacks'][item] += aantalSchalen;
                } else {
                    bestellingen['snacks'][item] = aantalSchalen;
                }
            } else {
                alert('Ongeldige invoer. Voer een geldig aantal in.');
            }
        } else {
            alert('U kunt alleen kiezen tussen 8 en 16 bitterballen.');
        }
    } else if (snack in prijzen) {
        const aantal = parseInt(prompt(`Hoeveel ${snack} wilt u toevoegen aan uw bestelling?`));
        if (!isNaN(aantal)) {
            if (snack in bestellingen['snacks']) {
                bestellingen['snacks'][snack] += aantal;
            } else {
                bestellingen['snacks'][snack] = aantal;
            }
        } else {
            alert('Ongeldige invoer. Voer een geldig aantal in.');
        }
    } else {
        alert('Sorry, dat hebben we niet. Probeer opnieuw.');
    }
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
