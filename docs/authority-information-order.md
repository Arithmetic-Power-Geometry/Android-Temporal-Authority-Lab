# Authority-Conditioned Information Order (ACIO)

## Motivation

Classical experiment comparison rewards information. Authorization-sensitive decision making can reverse that order because an experiment may be highly informative yet unavailable in precisely the worlds that remain possible.

Let E1 >=I E2 mean E1 is at least as informative as E2 by partition refinement. Let SafeResolve(E,C,g) mean E is admissible in every live world of C and its observations make the required decision g constant in every outcome cell.

## Authority-information reversal

An **authority-information reversal** occurs when

    E1 >=I E2,
    not SafeResolve(E1,C,g),
    SafeResolve(E2,C,g).

Thus raw informativeness is not monotone with authorization usefulness.

### Strict reversal theorem

There exist finite decision problems and experiments E1,E2 such that E1 strictly refines E2 observationally, yet E2 safely resolves the authorization decision and E1 cannot be executed under decision-neutral admissibility.

### Constructive proof

Take three worlds with decisions (deny, deny, allow). Let E1 have distinct outcomes in all three worlds but be inadmissible in the second. Let E2 merge the first two worlds, distinguish the third, and be admissible everywhere. E1 strictly refines E2. E2 loses state information but loses no decision-relevant information; because E2 is jointly admissible, it resolves the authorization decision. E1 does not. QED.

## Candidate principle: Authorized Blackwell failure

The result warns against importing an unconstrained informativeness ordering directly into authorization-sensitive agents. A more informative experiment can be dominated for the authorization task after admissibility is imposed.

This does NOT claim that Blackwell's theorem is false. It says the authorization-constrained feasible set changes the comparison problem. The research question is whether the induced preorder and its adaptive extension have already been characterized under another name.

## Connection to EAD

If EAD is the minimum safe information cost, adding a raw-more-informative but non-neutral probe need not decrease EAD. Adding a decision-neutral resolving probe can. Hence information quantity and safely usable information must be separated.

## Breakthrough gate

Do not promote ACIO on the finite reversal alone. Promotion requires:
1. proof of a nontrivial adaptive result;
2. reduction attack against constrained POMDPs, safe sensing, Blackwell comparison and epistemic authorization;
3. a result not obtainable merely by saying "constraints change the feasible set";
4. executable exhaustive counterexample search;
5. a domain consequence that distinguishes ACIO from existing models.
