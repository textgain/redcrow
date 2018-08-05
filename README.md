# Arabic Dialect Identifier (for RedCrow.co)

This is an automatic classification approach to identifying Arabic dialects. At this point, it is able to recognize distinguish between) two different dialects: Egyptian Arabic and Iraqi Arabic. More dialects will be added soon.

## Prerequisites
* Python2.7
* [scikit-learn](http://scikit-learn.org/) 0.19.1: 
`pip install sklearn`

## Usage guide

Import the `arabdialect` class:

`from arabicdialect import arabicdialect`

Then instantiate the classifier with one of these values: **egyptian**, **iraqi** and **multi**. So for example:

`ar = arabdialect('multi')`

There are two methods available: **classify_one** and **classify_many**. The former takes a single string as its argument, the latter takes an array of documents.

### Egyptian
The dialect-specific classifier for Egyptian returns boolean values, i.e. the document is classified as being either Egyptian (**True**) or Non-Egyptian (**False**).
```
from arabicdialect import arabicdialect
ar_eg = arabicdialect('egyptian')
non_egyptian_tweet = u'ما رتبت فوضاك غير الي نفت روحها في واد صمتك للأخير . غير ذي زرع ... ولكنه نبت  صار موطن للشعر حول الغدير  #وجد'
egyptian_tweet = u'-حبيبي إيه رأيك في عينيا في الشمس؟ =و الله أنا مش شايف في الشمس غير شنبك.'
print(ar_eg.classify_one(egyptian_tweet))
print(ar_eg.classify_one(non_egyptian_tweet))
print(ar_eg.classify_many([non_egyptian_tweet,egyptian_tweet]))
```

### Iraqi
The dialect-specific classifier for Iraqi returns boolean values, i.e. the document is classified as being either Iraqi (`True`) or Non-Iraqi (`False`).
```
from arabicdialect import arabicdialect
ar_ir = arabicdialect('iraqi')
non_iraqi_tweet = u'سب کا وقت مقرر ہے لیکن دعا ہے ہمارے اعمال ایسے ہوں کہ جب ہم دنیا سے جائیں تو لوگ دعا دیں نہ کہ خوش ہوں کہ برائی کم ہوئی'
iraqi_tweet = u'خوش امتحان اليوم كله غش 😂😂'
print(ar_ir.classify_one(iraqi_tweet))
print(ar_ir.classify_one(non_iraqi_tweet))
print(ar_ir.classify_many([non_iraqi_tweet,iraqi_tweet]))
```

### Multi
This classifier predicts whether a document is in *either* the Iraqi or the Egyptian dialect. It therefore does not return booleans, but either the class **iraqi** or **egyptian**.
```
from arabicdialect import arabicdialect
ar_multi = arabicdialect('multi')
egyptian_tweet = u'-حبيبي إيه رأيك في عينيا في الشمس؟ =و الله أنا مش شايف في الشمس غير شنبك.'
iraqi_tweet = u'خوش امتحان اليوم كله غش 😂😂'
print(ar_multi.classify_one(iraqi_tweet))
print(ar_multi.classify_one(egyptian_tweet))
print(ar_multi.classify_many([egyptian_tweet,iraqi_tweet]))
```

