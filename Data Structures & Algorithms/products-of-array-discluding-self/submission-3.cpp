class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 1);
        auto prev_acc = 1;
        // left to right
        for (auto i = 0; i < nums.size(); i++) {
            if (i == 0) {
                ;
            } else {
                res[i] *= prev_acc;
            }
            prev_acc *= nums[i];
        }
        // right to left
        prev_acc = 1;
        for (int i = static_cast<int>(nums.size())-1; i >= 0; i--) {
            if (i == nums.size()-1) {
                ;
            } else {
                res[i] *= prev_acc;
            }
            prev_acc *= nums[i];
        }
        return res;
    }
};
