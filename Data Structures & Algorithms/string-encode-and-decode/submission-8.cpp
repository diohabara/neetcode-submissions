class Solution {
public:
    string encode(vector<string>& strs) {
        string encoded;

        for (const auto& s : strs) {
            encoded += std::to_string(s.size()) + "#" + s;
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;

        size_t i = 0;

        while (i < s.size()) {
            size_t start = i;

            while (s[i] != '#') {
                i++;
            }

            size_t prefix_len = std::stoul(s.substr(start, i - start));

            i++; // after '#'

            res.push_back(s.substr(i, prefix_len));

            i += prefix_len;
        }

        return res;
    }
};