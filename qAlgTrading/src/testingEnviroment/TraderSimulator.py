class TraderSimulator:

    def performSimulation(self, trader, predictions, currentDayValue):
        trader_value = []
        trader_portfolio_value = []
        trader_capital_value = []
        trader_value.append(trader.currentTraderValue(currentDayValue[0]))
        trader_portfolio_value.append(trader.currentPortfolioValue(currentDayValue[0]))
        trader_capital_value.append(trader.currentCapital())
        for i in range(len(currentDayValue)):
            trader.actUponPrediction(currentDayValue[i], predictions[i])
            trader_value.append(trader.currentTraderValue(currentDayValue[i]))
            trader_portfolio_value.append(trader.currentPortfolioValue(currentDayValue[i]))
            trader_capital_value.append(trader.currentCapital())
        return {"trader_value": trader_value,"trader_portfolio_value": trader_portfolio_value,"trader_capital_value": trader_capital_value}