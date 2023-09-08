# Flashcards app
This program is similar to a language-learning app that uses flashcards. It shows a card with a word in the language the user wants to learn/revise and gives them 3 seconds to think of its translation.   
   
   ![Captura de ecrã 2023-09-08 151902](https://github.com/damachad/Python_exercises/assets/128734978/c46038d0-6c16-4d59-be7f-57eeb0411303)   
Then the user presses either the right or the wrong button (according to their given response). If they guessed correctly, then that word is removed from the words that appear on the cards, and a new file is created
with an updated version of the words to learn.   

   ![Captura de ecrã 2023-09-08 151908](https://github.com/damachad/Python_exercises/assets/128734978/fda817eb-48bc-4956-aeea-c10d56ada352)
   
**Note:** The default language to learn is set to be French and the answers are in English, but this program is customizable. For that, the user just has to get a CSV file with the words they wish to learn and substitute it 
with the "french_words.csv" inside the "data" folder. The interval between when the card is shown and the answer is revealed can also be changed (default is 3 seconds) by changing the correspondent constant in the code.

