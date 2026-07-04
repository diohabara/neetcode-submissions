class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> num_to_freq;
        for (auto& n : nums) {
            if (!num_to_freq.contains(n)) {
                num_to_freq[n] = 1;
            } else {
                return true;
            }
        }
        return false;
    }
};