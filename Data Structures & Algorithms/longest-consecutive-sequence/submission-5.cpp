class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> seen(nums.begin(), nums.end());

        int best = 0;

        for (int x : seen) {
            // x が連続列の開始点でないならスキップ
            if (seen.contains(x - 1)) {
                continue;
            }

            int len = 1;
            int cur = x;

            while (seen.contains(cur + 1)) {
                cur++;
                len++;
            }

            best = std::max(best, len);
        }

        return best;
    }
};