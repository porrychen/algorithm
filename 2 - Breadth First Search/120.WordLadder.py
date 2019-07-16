class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)

        queue, visited, distance = collections.deque([start]), set([start]), 0

        while queue:
            distance += 1

            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue

                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    def get_next_words(self, word):
        results = []

        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue

                results.append(left + char + right)

        return results
