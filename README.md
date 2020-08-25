# Text-summarizer-2
Text summarizer website, made with Django backend, Javascript/HTML/CSS front-end

To make this summarizer, I use the the concept of cosine similarity to calculate how similar each sentence is to one another. I add all the cosine similarities of one sentence (to other sentences) together to calculate the "similarity score" of the said sentence. Finally, I pick out the 3 lowest-score sentences and sort them by order in the original text.

First, you enter the text you wish to summarize. Click "submit" to begin summarizing. 

<img width="1086" alt="Screen Shot 2020-08-25 at 3 35 46 PM" src="https://user-images.githubusercontent.com/54921286/91234724-bc0d2280-e6e8-11ea-9543-5683b88516e0.png">

You will be redirected to the summary passage. 

<img width="1422" alt="Screen Shot 2020-08-25 at 3 35 50 PM" src="https://user-images.githubusercontent.com/54921286/91234726-bd3e4f80-e6e8-11ea-855d-0e4b31c858e9.png">
