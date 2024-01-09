function checkGuess(){
    const userGuess = Number(guessField.value);
    if (guessCount === 1) {
        guesses.textContent = "Previous guesses:";    
    }
    guesses.textContent = '${guesses.textContent} ${userGuess}';
    
    if (userGuess === randomNumber){
        lastResult.textContent = "Congratulations! You got it right!";
        lastResult.style.backgroundColor = "green";
    }
    
    
    
}