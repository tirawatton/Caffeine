package com.tonapps.caffeine.shared.format

import org.junit.Assert.assertEquals
import org.junit.Test
import java.math.BigDecimal

/** Same table as ios-app CurrencyFormatterTests.swift. */
class CurrencyFormatterTest {
    private val formatter = CurrencyFormatter()

    @Test fun whole() {
        listOf(
            Triple("6450", AmountSign.EXPENSE, "−฿6,450"),
            Triple("52000", AmountSign.INCOME, "+฿52,000"),
            Triple("1200.5", AmountSign.NEUTRAL, "฿1,201"),
            Triple("0", AmountSign.NEUTRAL, "฿0"),
        ).forEach { (raw, sign, expected) ->
            assertEquals(expected, formatter.whole(BigDecimal(raw), sign))
        }
    }

    @Test fun detail() {
        listOf(
            Triple("320", AmountSign.EXPENSE, "−฿320.00"),
            Triple("0.005", AmountSign.INCOME, "+฿0.01"),
        ).forEach { (raw, sign, expected) ->
            assertEquals(expected, formatter.detail(BigDecimal(raw), sign))
        }
    }
}
