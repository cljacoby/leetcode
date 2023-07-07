#include "vector"
#include "unordered_map"
#include "assert.h"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int diff = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (map.count(diff) == 1) {
                int j = map[diff];
                return vector<int> {i, j};
            }
            map.insert({nums[i], i});
        }

        assert(false && "Should not get here");
    }
};

int main(void) {
    
    vector<int> nums = {2,7,11,15};
    int target = 9;
    vector<int> solution = {1,0};
    Solution sol;
    vector<int> result = sol.twoSum(nums, target);
    assert(result == solution);
}
