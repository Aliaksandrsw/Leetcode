class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        q = []

        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                q.insert(i, 'FizzBuzz')

            elif i % 3 == 0:
                q.insert(i, 'Fizz')

            elif i % 5 == 0:
                q.insert(i, 'Buzz')
            else:
                q.insert(i, str(i))

        return q