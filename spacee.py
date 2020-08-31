from DataReader import DataReader
from TweetNormalizer import normalizeTweet
import torch
import tqdm
import _pickle as cPickle
from pprint import pprint
import spacy
import wikipedia
from wikipedia2vec import Wikipedia2Vec
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
nlp = spacy.load("en_core_web_sm")
'''
dr = DataReader('./Data/olid-training-v1.0.tsv','A')
data,labels = dr.get_labelled_data()
data = data[:]
'''
dr_tst = DataReader('./Data/testset-levela.tsv','A')
tst_data,tst_label = dr_tst.get_test_data()

data = tst_data[:]
labels = tst_label[:]

entities = []
for line in tqdm.tqdm(data):
    temp = []
    doc = nlp(normalizeTweet(line))
    for chunk in doc.noun_chunks:
        if chunk.text!="@USER" and chunk.text!="HTTPURL" and chunk.text not in stop_words:
            res = wikipedia.search(chunk.text,results=2)
            for term in res:
                temp.append(term)
    entities.append(temp)
print(len(entities))
print(len(entities[0]))
with open('./pickles/spacentest.pkl','wb') as f:
    cPickle.dump(entities,f)


'''
wiki2vec = Wikipedia2Vec.load('/data/users/abhavan/enwiki_20180420_100d.pkl')
f = open('pickles/entities.pkl','rb')
entities = cPickle.load(f)

wiki_vectors = []

x = ['Native Americans in the United States', 'Native American slave ownership']
temp = []
for sent in x:
    arr = wiki2vec.get_entity_vector(sent)
    torcharr = torch.from_numpy(arr)
    torcharr = torcharr.unsqueeze(0)
    print(torcharr.shape)
    print(sent)
    temp.append(torcharr)

res = torch.mean(temp,dim=0)
print(res.shape)

for sent in tqdm.tqdm(entities):
    temp = []
    for entity in sent:
        arr = wiki2vec.get_entity_vector(entity)
        torcharr = torch.from_numpy(arr)
        torcharr = torcharr.unsqueeze(0)
        temp.append(torcharr)
    wiki_vectors.append(torch.mean(temp,dim=0))

'''





