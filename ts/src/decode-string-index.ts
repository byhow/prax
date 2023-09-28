// function decodeAtIndex(s: string, k: number): string {
//     let decoded_len = 0

//     for (const c of s) {
//         if (isNumeric(c)) {
//             decoded_len *= parseInt(c)
//         } else {
//             decoded_len+=1
//         }
//     }

//     for (let i = s.length - 1; i >= 0; i--) {
//         const curr = s[i]
//         if (isNumeric(curr)) {
//             decoded_len = Math.floor(decoded_len / parseInt(curr));
//             k %= decoded_len
//         } else {
//             if (k === 0 || decoded_len === k) {
//                 return curr
//             }
//             decoded_len-=1
//         }
//     }

//     return ''
//     // if (k < 1) {
//     //     return ''
//     // }
//     // let decoded = ''
//     // let curr = 0;
//     // while (curr < s.length) {
//     //     // console.log(decoded)
//     //     if (isNumeric(s[curr])) {
//     //         let temp = ''
//     //         for (let i = 0; i < parseInt(s[curr]); i++) {
//     //             // console.log(decoded, temp, curr, s[curr])
//     //             temp = temp.concat(decoded)
//     //         }
//     //         decoded = temp;

//     //     } else {
//     //         decoded = decoded.concat(s[curr])
//     //     }
//     //     curr++
//     //     if (curr > k) {
//     //         return decoded[k - 1]
//     //     }
//     // }
//     // return decoded[k - 1]
// };

function decodeAtIndex(inputString: string, k: number): string {
  let decodedLength = 0; // Total length of the decoded string

  for (const char of inputString) {
    if (/\d/.test(char)) {
      // If the character is a digit, update the decoded length accordingly
      decodedLength *= parseInt(char, 10);
    } else {
      // If the character is a letter, increment the decoded length
      decodedLength += 1;
    }
  }

  // Traverse the input string in reverse to decode and find the kth character
  for (let i = inputString.length - 1; i >= 0; i--) {
    const currentChar = inputString[i];

    if (/\d/.test(currentChar)) {
      // If the character is a digit, adjust the length and k accordingly
      decodedLength = Math.ceil(decodedLength / parseInt(currentChar, 10));
      k %= decodedLength;
    } else {
      // If the character is a letter, check if it's the kth character
      if (k == 0 || decodedLength == k) {
        return currentChar; // Return the kth character as a string
      }

      decodedLength -= 1;
    }
  }

  return ''; // Return an empty string if k is out of range
}

const isNumeric = (c: string): boolean => /\d/.test(c);
