# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Initially, the game is very simple and did not work. There were bugs with the the hints being wrong, higher and lower were swapped. Also, the game would not restart, attempts would remain the same, but secret number would change.

## 2. How did you use AI as a teammate?

I used Claude. The AI suggested me various bug fizes and its thought processes behind its decisions. Calude suggested correctly implemented fixes for the difficulty class, reccomending to use wariables like high and low instead of a hard coded range. I verified this by testing the game and seeing how the range for difficulty is outputted. One error Claude made was when fixing the attempts, the counter did not go down for the first attempt, but still counted as an attempt and would display 1 attempt left after all attempts were used. I checked this by seeing that even when 6 out of 6 attempts are used, since the counter doesn't go down for the first attempt, it still says 1 attempt left.

## 3. Debugging and testing your fixes


When the calculation and the tracing of the expected output matched the actual output; I was able to tell it was fixed. Also, I tried my own implemntation aswell to compare which was btter. I ran tests on the attempts counter to fix the method and when it updated the counted, subracting from attempts left and adding to debug attempts made. This showed that my code had some imperfections even with AI. Claude helped design test cases. I prompted it to come up with various cases.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because of how streamlit works. It reruns the entire script whenever there is any new ineraction with the UI. Since the randint for the secret number wasn't being checked to see if it already had a stored value, it would generate a new value every time. If i were to explain Streamlit "reruns" and sessions states to a friend, I would tell them that its like losing your memory and starting with a blank slate every time you want to do something. The change I made to make secret number stabe is inserting an if statement which chekcs if "secret" is not alrady in the session state. If it isn't, only then does it generate a new secret number. This avoids it regenerating everytime there is interacton, and only regenerates on a new game.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
