# Text-summarizer-2
Text summarizer website, made with Django backend, Javascript/HTML/CSS front-end

To make this summarizer, I use the the concept of cosine similarity to calculate how similar each sentence is to one another. I add all the cosine similarities of one sentence (to other sentences) together to calculate the "similarity score" of the said sentence. Finally, I pick out the 3 lowest-score sentences and sort them by order in the original text.
