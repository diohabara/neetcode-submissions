class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        std::sort(nums.begin(), nums.end());
        auto last_num = nums[0];
        auto cur = 1; // current streak
        auto ma = 1; // max streak
        for (size_t i = 1; i < nums.size(); i++) {
            if (last_num == nums[i]) {
                continue;
            } else if (nums[i] == last_num+1) {
                last_num = nums[i];
                cur++;
                ma = std::max(cur, ma);
            } else {
                last_num = nums[i];
                cur = 1;
            }
        }
        return ma;
    }
};
