#mapを使うリストの全てに関数を適応させたい時に使う。
#map (function,iterable) functionには関数オブジェクト、iterableにはリストやタップルのデーター型を持って来る

nums= [1,2,4,5,6]
x2 = lambda x : x*2
list (map(x2,nums))

#filter リストから任意の要素を取り出す時に使う
#filter(function,iterable) functionには関数オブジェクト、iterableにはリストやタップルのデーター型を持って来る

nums2= [1,2,4,5,6]
#偶数のみ抽出
list (filter(lambda x : (x%2) == 0,nums2))