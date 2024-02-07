def frequencySort(self, s):
      hashMap = {}
      result = []
      final = ""
      for i in s:
          hashMap[i] = hashMap.get(i, 0) + 1
      collection = list(hashMap.keys())
      for j in collection:
          result.append({"key":j, "value":hashMap[j]})
      result=sorted(result, key=lambda d: d["key"])
      result=sorted(result, key=lambda d: d["value"], reverse = True)    
      for k in result:
          final += k["key"] * k["value"]
      return final
