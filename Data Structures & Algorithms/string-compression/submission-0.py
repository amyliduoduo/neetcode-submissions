class Solution:
    def compress(self, chars: List[str]) -> int:
        #Initialize two pointers: read for identifying the same character, write for the position of compressed result to be written
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read] #char is the current element we read
            start = read #initialize start to the initial read pointer

            # Find the end of this group by moving read pointer past all the first round of the same characters
            while read < len(chars) and chars[read] == char:
                read += 1

            #get the frequency of the character
            count = read - start

            # Write the character
            chars[write] = char
            write += 1 #move the pointer to the next round

        # Write the count if > 1 
            if count > 1:
                for digit in str(count): #convert the integer to string
                    chars[write] = digit
                    write += 1

        return write