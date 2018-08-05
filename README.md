# Arabic Dialect Identifier (for RedCrow.co)

This is an automatic classification approach to identifying Arabic dialects. At this point, it is able to recognize distinguish between) two different dialects: Egyptian Arabic and Iraqi Arabic. More dialects will be added soon.

## Usage guide




### Egyptian

```
ar_eg = arabicdialect('egyptian')
non_egyptian_tweet = u'ما رتبت فوضاك غير الي نفت روحها في واد صمتك للأخير . غير ذي زرع ... ولكنه نبت  صار موطن للشعر حول الغدير  #وجد'
egyptian_tweet = u'-حبيبي إيه رأيك في عينيا في الشمس؟ =و الله أنا مش شايف في الشمس غير شنبك.'
print(ar_eg.predict_one(egyptian_tweet))
print(ar_eg.predict_one(non_egyptian_tweet))
print(ar_eg.predict_many([non_egyptian_tweet,egyptian_tweet]))
```

### Iraqi

