# Interview-answer sample: How does `@Transactional` work?

## Weak answer

> `@Transactional` opens a transaction and rolls it back when an error happens.

Why it is weak:

- it describes only the annotation’s surface behaviour;
- it does not explain proxy interception;
- it ignores transaction-manager selection and propagation;
- it overstates rollback behaviour;
- it gives no production example or failure mode.

## Acceptable answer

> In a typical Spring application, `@Transactional` is applied through a proxy. When another bean calls the proxied method, the interceptor asks the configured transaction manager to start or join a transaction. It commits when the method completes successfully and normally rolls back for unchecked exceptions. Propagation and isolation can change that behaviour.

Why it is acceptable:

- explains proxy interception;
- mentions start or join behaviour;
- qualifies rollback behaviour;
- mentions propagation and isolation.

## Strong answer

> In the common proxy-based model, Spring wraps the bean and intercepts external calls to a `@Transactional` method. The interceptor resolves the transaction attributes, asks the selected `PlatformTransactionManager` to create or join the transaction, binds the relevant resources to the current thread, invokes the method, and then commits or rolls back according to the configured rules. A common trap is self-invocation: one method calling another method on the same instance bypasses the proxy, so the inner annotation may not take effect. I also avoid holding a transaction open across slow network calls because the database connection can remain checked out and contribute to pool exhaustion. I validate transaction behaviour with integration tests rather than assuming the annotation is active.

Why it is strong:

- explains the runtime mechanism;
- identifies self-invocation;
- connects transaction scope to production behaviour;
- avoids claiming that every exception automatically rolls back;
- includes a validation strategy.

## Follow-up questions

1. What changes with `REQUIRES_NEW`?
2. When can a checked exception trigger rollback?
3. Why can a private transactional method be ineffective in proxy mode?
4. How would you detect a transaction that remains open during an external API call?
5. What is the difference between transaction isolation and propagation?
