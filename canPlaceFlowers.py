def canPlaceFlowers(self, flowerbed, n):
      count = 0
      i = 0
      while i < len(flowerbed):
          if flowerbed[i] == 0:
              next_plot = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
              prev_plot = 0 if i == 0 else flowerbed[i - 1]

              if next_plot == 0 and prev_plot == 0:
                  flowerbed[i] = 1
                  count += 1
                  i += 2  
              else:
                  i += 1  
          else:
              i += 2  

      return count >= n
