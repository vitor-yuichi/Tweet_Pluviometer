Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#This fuction counts the frequency of a list ofwords in a DATE type DATA
#text: list of the text 
#data_fraq: is a list of how many times each date repeat
#list_words: Is a list of the words that you want to search 
def meteo_temporal_distribution(text,data_fraq,list_words):
  y=[0]*len(data_fraq)
  aux=0
  aux1=0
  i=0
  count=0
  while i<len(data_fraq): 
    for l in range (0, data_fraq[i]):
      for k in range(0,len(list_words)): 
        if (re.search(list_words[k], text[aux], re.IGNORECASE)!=None):
          count=count+1
      aux=aux+1
      aux1=aux1+1
      if aux1==(data_fraq[i]):
        y[i]=count
        aux1=0
        count=0
    i=i+1
  return y
