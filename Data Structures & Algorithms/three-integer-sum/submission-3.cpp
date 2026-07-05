class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());

        int n = nums.size();

        for (int i = 0; i < n; i++) {
            // 同じ nums[i] を固定すると重複 triplet になるのでスキップ
            if (0 < i && nums[i-1] == nums[i]) continue;

            // nums[i] が正なら、以降も全部 >= nums[i] なので 0 は作れない
            if (0 < nums[i]) break;

            int l = i + 1;
            int r = n - 1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) {
                    ans.push_back({nums[i], nums[l], nums[r]});

                    l++;
                    r--;

                    // 左右それぞれ同じ値を飛ばして重複防止
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;
                }
                else if (sum < 0) {
                    // もっと大きい値が必要
                    l++;
                }
                else {
                    // もっと小さい値が必要
                    r--;
                }
            }
        }

        return ans;
    }
};
