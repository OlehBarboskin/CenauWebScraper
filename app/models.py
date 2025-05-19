import os
import json
import pandas as pd
import numpy as np
class Product:
    def __init__(self):
        pass

class Opinion:
    selectors = {
        "opinion_id": (None, "data-entry-id"),
        "author": ("span.user-post__author-name",),
        "recommendation": ("span.user-post__author-recomendation > em",),
        "stars": ("span.user-post__score-count",),
        "content_pl": ("div.user-post__text",),
        "pros_pl": ("div.review-feature__item--positive", None, True),
        "cons_pl": ("div.review-feature__item--negative", None, True),
        "vote_yes": ("button.vote-yes","data-total-vote"),
        "vote_no": ("button.vote-no","data-total-vote"),
        "published": ("span.user-post__published > time:nth-child(1)","datetime"),
        "purchased": ("span.user-post__published > time:nth-child(2)","datetime"),
    }

    def __init__(self, opinion_id ="", author="", recommendation=False, stars=, content, pros, cons, vote_yes, vote_no, publish_date, purchase_date):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.vote_yes = vote_yes
        self.vote_no = vote_no
        self.publish_date = publish_date
        self.purchase_date = purchase_date
    
    def __str__(self):
        return "\n".join([f"{key}: {getattr(self, key)}" for key in self.selectors.keys()])
    
    def __repr__(self):
        return "Opinion("+", ".join([f"{key}={str(getattr(self, key))}" for key in self.selectors.keys()])+")"
    
    
    def export_info(self):
        if not os.path.exists("app/data"):
            os.mkdir("./app/data")
        if not.os.path.exists("./app/data/products"):
            os.mkdir("./app/data/products")
        with open(f".app/data/products/{self.product_id}.json","w", encoding ="UTF-8") as jf:
            json.dump(, jf, ensure_ascii=false, indent=4)\

    def import_opinions(self):
        with open (f".app/data/opinions/{self.product_id}.json", "r", encoding = "UTF=8")as jf:
            opinions = json.load(jf)
        for opinion in opinions:
            single_opinions.append(single_opinon)

    def import_info (self):
        with open (f".app/data/products/{self.product_id}.json", "r", encoding = "UTF-8") as jf:
            info = json.load(jf)
        self.product_name = info ['product_name'
        ]


    def analyze(self):
        opinions = pd.DataFrame.from_dict({opinon.transform_to_dict() for opinion in self.opinons})
        self.stats["opinons_count"] = opinons.shape[0]
        self.stats["pros_count"] = 

    class Opionions:
        selectors   = {
            self.stats."opinions_id": (None, "data-entry-id")
            self.stats."author": ("span.user")
        }    


        