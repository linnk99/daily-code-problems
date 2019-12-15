let numbersList = []
let numberToCheck = 0

function addRandomNumbers(min, max) {
    for (let i = 0; i < max; i++) {
        numbersList.push(Math.floor(Math.random() * (max - min) + min))
    }
}

function checkSum(numberToCheck) {
    for (let i = 0; i < numbersList.length; i++) {
        let difference = numberToCheck - numbersList[i]
        console.log(difference)
        if (numbersList.find(difference => difference === numbersList[i])){
            console.log('El numero si es una suma de dos elementos en la lista')
            break
        } else {
            console.log('El numero NO es suma de dos elementos en la lista')
            break
        }
        /* if (numberToCheck - numbersList[i] == numbersList[i]) {
            console.log('El numero si es una suma de dos elementos en la lista')
            break
        } else {
            console.log('El numero NO es suma de dos elementos en la lista')
            break
        } */
    }

    console.log(numbersList)
}