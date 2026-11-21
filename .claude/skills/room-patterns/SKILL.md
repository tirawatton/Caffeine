---
name: room-patterns
description: Room rules for Caffeine - entities matching the logical model, String-backed BigDecimal converter, DAOs with Flow, repository interfaces, explicit migrations, in-memory tests. Read by android-developer, backend-lead.
---

# Room Patterns

```kotlin
@Entity(tableName = "transactions", indices = [Index("categoryId"), Index("date")])
data class TransactionEntity(
    @PrimaryKey val id: String,          // UUID string, same value space as iOS
    val amount: BigDecimal,              // via BigDecimalConverter (String) - never Double
    val currencyCode: String = "THB",
    val type: String,                    // expense | income | transfer
    val categoryId: String?,
    val accountId: String,
    val date: Long,                      // epoch millis UTC; month maths in ZoneId.systemDefault()
    val note: String? = null,
)

class BigDecimalConverter {
    @TypeConverter fun from(v: BigDecimal?): String? = v?.toPlainString()
    @TypeConverter fun to(v: String?): BigDecimal? = v?.let(::BigDecimal)
}
```

- Field names match the logical model and the SwiftData mapping.
- DAOs return `Flow` for observed lists and `suspend` for one-shot reads/writes. Typed queries only.
- Repository interface in `repository/`, Room implementation `RoomXxxRepository` with an injected IO dispatcher; maps entities to domain models.
- `exportSchema = true`; schemas committed under `android-app/app/schemas/`. Every version bump has an explicit `Migration` and a `MigrationTestHelper` test. Never `fallbackToDestructiveMigration()` in release.
- Tests: `Room.inMemoryDatabaseBuilder` in `androidTest`.
