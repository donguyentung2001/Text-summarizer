from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from nltk import tokenize

def summarize(text): 
    stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    sentences=tokenize.sent_tokenize(text) 
    indexes=[]
    for i in range(len(sentences)): 
        indexes.append(i) 
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(sentences)
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names(), index=indexes)
    for (columnName, columnData) in df.iteritems(): 
        if columnName in stop_words: 
            df=df.drop(columns=columnName)
    similarity_list=cosine_similarity(df, df)
    similarity_list_sums=[]
    for i in range(len(similarity_list)): 
        similarity_list_sums.append(sum(similarity_list[i]))
    similar_sort=sorted(similarity_list_sums)
    new_sentences=[]
    for j in range(len(similarity_list_sums)): 
        if similarity_list_sums[j] in similar_sort[-3:]: 
            if sentences[j] not in new_sentences:
                new_sentences.append(sentences[j])
    summary=" ".join(new_sentences)
    return summary 