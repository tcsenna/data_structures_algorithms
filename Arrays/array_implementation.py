class MyArray:
    def __init__(self):
        self.length=0
        self.data={}
    def __str__(self):
        return str(self.__dict__)
    def get(self, index):
        return self.data[index]
    def push(self, item):
        # adiciona um elemento no final do array
        self.data[self.length]=item
        self.length+=1
    def pop(self):
        # Verifica se o array está vazio
        if self.length == 0:
            return None  # Retorna None se o array estiver vazio
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    def delete(self,index):
        deleted=self.data[index]
        for i in range(index,self.length-1): #I've started looping over things, which makes the operation O(n)
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
        return deleted   

    
arr=MyArray()
arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
arr.delete(3)
print(arr)
        
        
    
        
    


   