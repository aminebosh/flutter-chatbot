import json
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

intents = json.load(open('intents2.json','r'))
intents2 = json.load(open('intents2_questions.json','r'))

conditions=[]
symptoms=[]
for intent in intents['intents']:
    conditions.append(intent['tag'])
    symptoms.append(intent['patterns'])
    
    
index2=[]
questions2=[]
for intent in intents2['intents']:
    for pattern in intent['patterns']:
        questions2.append(pattern)
        index2.append(intent['question_type'])

count_vectorizer = CountVectorizer(stop_words='english')
data=symptoms


def most_similar(message,data,target):
    data = [message]+data
    index = ['message'] + target
    vector_matrix = count_vectorizer.fit_transform(data)
    cosine_similarity_matrix = cosine_similarity(vector_matrix)
    df = pd.DataFrame(data=cosine_similarity_matrix, index=index, columns=index)
    dict={'name':df['message'].nlargest(2).index[1],'similarity':df['message'].nlargest(2)[1]}
    return dict


class Response:
    condition=''
    def get_response(self,message):
        dict=most_similar(message,data,conditions)
        print(dict)
        if dict['similarity'] > 0.35:
            self.condition=dict['name']
            for intent in intents['intents']:
                        if intent['tag']==self.condition:
                            result=intent['responses']
                            result ="These symptoms might be an indication of "+self.condition+".\n"+result
                            break
        else :
            dict=most_similar(message,questions2,index2)
            print(dict)
            if dict['similarity'] > 0.4:
                for intent in intents2['intents']:
                    if intent['question_type']==dict['name']:
                        result=intent['responses'][self.condition]
                        break
            else :
                result ="I'm sorry, I couldn't understand you."
        return result