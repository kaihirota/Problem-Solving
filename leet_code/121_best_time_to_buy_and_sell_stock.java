// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
  public int maxProfit(int[] prices) {
    int maximumProfit = 0;
    for (int i = 0; i < prices.length - 1; i++) {
      for (int j = i + 1; j < prices.length; j++) {
        maximumProfit = Math.max(maximumProfit, prices[j] - prices[i]);
      }
    }
    return maximumProfit;
  }

  public int maxProfitSolution(int prices[]) {
    int minprice = Integer.MAX_VALUE;
    int maxprofit = 0;
    for (int i = 0; i < prices.length; i++) {
        if (prices[i] < minprice)
            minprice = prices[i];
        else if (prices[i] - minprice > maxprofit)
            maxprofit = prices[i] - minprice;
    }
    return maxprofit;
}
}

public class Main {
  public static void main(String[] args) {
    int arr1[] = {7, 1, 5, 3, 6, 4};

    int ret = new Solution().maxProfit(arr1);
    System.out.println(ret);
  }
}