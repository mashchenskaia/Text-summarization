# код используется для извлечения чистого текста вне таблиц из документов .docx
# и для токенизации полученного текста на предложения
# для подгонки под домен документа используйте кастомный набор сокращений
# контактное лицо - Скворцова Екатерина (+79162804322)


import pandas as pd
from rusenttokenize import ru_sent_tokenize
from docx.api import Document
import docx

class SentTokenizer:
    def __init__(self):
        self.pure_text = None
    
    def _sentence_collection(text_without_tables):
        shortenings_ = {'зав', 'куб', 'о', 'тыс', 'мин', 'букв', 'обл', 'сек', 'русск', 'зам', 'коп',
                        'повел', 'яз', 'прим','гос', 'муж', 'обр', 'ед', 'рус', 'га', 'искл', 'дол', 'долл',
                        'авт', 'corp', 'корп', 'мн', 'жен', 'адм', 'ред', 'лат', 'проц', 'бб', 'сзб', 
                        'р','таб', 'мэр', 'юл','ува','срб', 'двб','ува','нжя','ца','юзб', 'ул', 'евр', 'наст',
                        'км','кп','инн','госб','ук','ип','всп','госб','ооо','пао','гк','пм','всп', 'внд'}

        #joining_shortenings_={'пл', 'см', 'св', 'кит', 'устар', 'стр', 'пер', 'ул', 'евр',
        #                  'г', 'слав', 'им', 'д', 'тел', 'корп', 'рис', 'п', 'наст',"дог",'т','ч',
        #                  'гг','увдо','доп','руб','млн','тыс', 'юр','физ','таб', 'рук', 'т.ч.', 'т.ч', 'т ч',
        #                 'кв','эл',"м","с","т",'эт','мес','яр',"шт","млн", 'тыс','руб', 'cм', 'см'}
        
        joining_shortenings_={}
        
        paired_shortenings_={('т', 'п'), ('т', 'е'), ('у', 'е'), ('н', 'э'), ('и', 'о'), ('т','к'),('т','д'),('д','в'),
                            ('т','ч'),('с','м')}
        sentences = []
        for sentence in text_without_tables:
            sentences.append(ru_sent_tokenize(sentence, 
                        shortenings = shortenings_,
                        joining_shortenings=joining_shortenings_,
                        paired_shortenings=paired_shortenings_))
        sentences=[j for i in sentences for j in i]
        sentences = [i for i in sentences if len(i)>0]
        return sentences
    
            
    def _text_without_tables(self, document):
        """
        Params:
            document: docx.api.Document

        Returns:
            text_without_tables: list
        """
        text_without_tables = []
        for para in document.paragraphs:
            text_without_tables.append(para.text)
        text_without_tables=[i for i in text_without_tables if len(i)>0]
        text_without_tables =[i.replace('\t','') for i in text_without_tables]
        self.pure_text = text_without_tables
        return text_without_tables