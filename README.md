# policy_value

life stats are based on:
https://www.ssa.gov/oact/STATS/table4c6.html

models are based on, not exactly same:
https://www.diva-portal.org/smash/get/diva2:426603/FULLTEXT02

The first step in the stochastic method is the modification of the mortality table for each
individual in order to reflect that individual’s mortality risk. Each policy in the pool has
to be connected with a standard mortality table (see for example Table 1), with the risk
associated with each individual corresponding to one row of the standard mortality table
for his or her age at the time of settlement and with the probabilities of death after that
age. Their life expectancy is then used to calculate a mortality multiple which will be
used to adjust these probabilities for individual mortality risk. In the end one table
which contains the adjusted probabilities of death for each individual is formed (see for
example Table 2). This will be the table whose elements will be used in the simulation
process. 

Second step: Monte Carlo simulation of the time of death
When each policy has been linked with the adjusted probabilities of death, i.e. the
adjusted or impaired mortality table of all policies in the pool has been created; Monte
Carlo simulation is employed in order to project when each individual dies. For a given
year a uniformly distributed random number17 between 0% and 100% is draw.
Subsequently, this number is compared with the probability of death for a policyholder
at that given year as it is given by the impaired mortality table. If the random number is
less than or equal to the probability of death, the policyholder is assumed to be dead,
hence, the premium payment stops and the death benefit is received. Otherwise, the
policyholder is assumed to be alive, the premium payment continues for the next year, 

Third step: Cash flows
The final step on the pricing of the value of a portfolio of life settlements is the
aggregation of the projected cash flows that each policy in the pool produces. Let Xi
 be
the probability of death for a policy in year i, Yi
 the random number that is drawn from
the Monte Carlo simulation, where Yi
 ~ i.i.d U(0,1), and CFi
 the cash flow that accrues
from this policy, which can be either the premium, p, or the death benefit, B, after
paying the premium. This is shown in the expression:

When the third step of the method is finished, we end up having a row vector whose
elements are the projected net cash flows, i.e. total death benefits received (cash
inflows) minus total premia (cash outflows) of the portfolio for each year until the
maturity of the portfolio. These net cash flows can be used in order to calculate the
present value of the portfolio. This can be done by discounting the net cash flows of the
portfolio for each year. Thus, the present value of the portfolio will be a function of the
discount rate which ultimately reflects the investors’ demanded rate of return on their
investment. The analysis that follows in part 4.3 on the discount rate and the present
value of a portfolio of life settlements will provide an understanding on how life
settlements are priced and which factors have to be taken into account in order to
postulate whether the life settlement transactions are priced on their fair value based on
our knowledge about the balance between risk and return that investors demand.
However, before that, on part 4.2 some considerations are provided regarding the
understanding of risk that a pool of life settlement entails.
