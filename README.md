3rd party estimation (i think bit under valued)
https://www.apexlifesettlements.com/estimate


some knowledge:
- Considering that the average annual premiums for a term life insurance policy of $500,000 is between $8,000 and $9,500 for men and women aged 70 or older. (1.6-1.9%)
- Surrendering a policy typically has a return of $469 per $100,000 (less than 0.5% compared to 20% from a life settlement). 

qulifacation:
- Policy Age: To qualify for a life settlement, you must have held your current policy for at least 2 years.
- Death Benefit: Your death benefit must be at least $100,000.
- Age: You must be at least 65 years old to be eligible for a life settlement, and ideal candidates are typically 75 or older. 
- Lifespan: You must have experienced a change in health and have a life expectancy of less than 15 years to qualify.

https://www.lsa-llc.com/life-settlement-calculator/


What Happens If Your Insurance Company Goes Out Of Business?
- state guaranty association will pay up to 300k for life insurance

https://www.forbes.com/advisor/life-insurance/company-out-of-business/


Life Settlement Industry Statistics for 2023
- The average life insurance policy has a face value of $168,000
- 85% or more of life insurance policies don’t pay a death benefit: Statistically speaking, 85% of term policies and 88% of universal life policies will expire, lapse, or be surrendered before a death benefit is paid.
- $200 billion worth of life insurance will be surrendered or lapsed annually through 2027: Even as closed settlements and third-party analyses continue to confirm that life settlements generate higher proceeds for policyholders, people still choose to lapse or surrender their life insurance. In many cases, these policyholders simply don’t know that selling their policy is an option.
- More than half of Americans don’t know they can sell their life insurance: More than half (55%) of Americans aren’t familiar with life settlements and more than two-thirds (68%) of Americans aren’t familiar with viatical settlements.
- The life settlement industry is growing 34% per year on average: The life settlement industry is poised to grow substantially in the coming years. Contributing factors include an aging population and generally low balances in retirement savings accounts. Between 2015 and 2025, the U.S. senior population will grow by 38%, and many of those seniors won’t have sufficient retirement savings to replace their working income. Those who have life insurance — estimated to be 50% of seniors — can liquidate those life insurance assets to produce much-needed funding for retirement.
- $37.5 billion in lost wealth for seniors: The projected $200 billion in life insurance that will be lapsed or surrendered each year is potentially worth $50 billion on the life settlement market. That assumes a payout rate of 25%, the midpoint of the typical life settlement payout range of 20% to 30% of the policy’s face value. 

https://www.harborlifesettlements.com/life-insurance-settlements-and-settlement-statistics/


Life Settlement Regulations
The momentum in life settlements caught the attention of state regulators in the
late 1990s. The industry has since been shaped by state regulations as well as:
- The Life Settlements Model Act, adopted by the National Conference of
Insurance Regulators (NCOIL) in 2000. The act lays out requirements for
contracts, disclosures, and reporting. It also specifies licensing requirements
for agents and providers and describes prohibited business practices.
- The Life Insurance Consumer Disclosure Model Act, adopted by NCOIL in
2010, which mandates written disclosures to seniors in danger of policy
lapse.
- Tax Cuts and Jobs Act, signed into law in 2017, which defined a more
favorable tax treatment for life settlements.
- State-imposed waiting periods and disclosure laws. Eight states require life
insurers to tell policyowners about life settlements before they surrender or
lapse their policy. Thirty-three states have waiting periods, meaning a policy
must be in force for a minimum duration before it can be sold. A
state-mandated waiting period prevents people from buying insurance solely
for the purpose of selling it. These waiting periods range from two to five
years.

https://www.harborlifesettlements.com/wp-content/uploads/2022/02/Harbor_Life_Settlements_Whitepaper.pdf


LIFE EXPECTANCY ESTIMATES
Life expectancy estimates or "LEs" are issued as part of a mortality report prepared by a third-party life expectancy underwriter and are required during the life settlement process.
These 4 companies that commonly issue life expectancy reports in the life settlement industry:
- 21st Services, LLC
- AVS Underwriting, LLC
- Fasano & Associates, LLC
- Examination Management Services, Inc.

https://www.welcomefunds.com/life-settlement-glossary/life-expectancy.html


low correlation and active management is the key

https://airassetmanagement.com/insights/volatility-high-low-life-settlement-strategies-perform


AAP Life Settlement Valuation - ‘Fair Value’-Valuation
A majority of the projected IRR are in a band between about 10% and 25%, with a few outliers under 10% and over 25%. The average projected IRR of the whole sample is 19.4%. However the average projected IRR of the secondary market transactions is 20.3%, the respective number for tertiary market transactions is 18.1%

https://www.aa-partners.ch/fileadmin/files/Valuation/AAP_Life_Settlement_Valuation_-_Manual_V6.0.pdf


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

to do:
add a default % for each insurance co. 
