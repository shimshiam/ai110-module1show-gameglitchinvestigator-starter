# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Initially, the game is very simple and did not work. There were bugs with the the hints being wrong, higher and lower were swapped. Also, the game would not restart, attempts would remain the same, but secret number would change.

## 2. How did you use AI as a teammate?

I used Claude. The AI suggested me various bug fizes and its thought processes behind its decisions. Calude suggested correctly implemented fixes for the difficulty class, reccomending to use wariables like high and low instead of a hard coded range. I verified this by testing the game and seeing how the range for difficulty is outputted. One error Claude made was when fixing the attempts, the counter did not go down for the first attempt, but still counted as an attempt and would display 1 attempt left after all attempts were used. I checked this by seeing that even when 6 out of 6 attempts are used, since the counter doesn't go down for the first attempt, it still says 1 attempt left.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
