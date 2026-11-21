package com.tonapps.caffeine.shared.format

import java.math.BigDecimal
import java.math.RoundingMode
import java.text.DecimalFormat
import java.text.DecimalFormatSymbols
import java.util.Locale

/** Mirror of ios-app CurrencyFormatter.swift — outputs must match string for string. */
enum class AmountSign { EXPENSE, INCOME, NEUTRAL }

class CurrencyFormatter(private val currencyCode: String = "THB") {

    /** Whole baht for lists and heroes, e.g. "−฿6,450". */
    fun whole(amount: BigDecimal, sign: AmountSign): String = format(amount, 0, sign)

    /** Two decimals for detail, edit and slip review, e.g. "−฿320.00". */
    fun detail(amount: BigDecimal, sign: AmountSign): String = format(amount, 2, sign)

    private fun format(amount: BigDecimal, fractionDigits: Int, sign: AmountSign): String {
        val rounded = amount.abs().setScale(fractionDigits, RoundingMode.HALF_UP)
        val pattern = if (fractionDigits == 0) "#,##0" else "#,##0." + "0".repeat(fractionDigits)
        val number = DecimalFormat(pattern, DecimalFormatSymbols(Locale.US)).format(rounded)
        val symbol = if (currencyCode == "THB") "฿" else "$currencyCode "
        val prefix = when (sign) {
            AmountSign.EXPENSE -> "−"
            AmountSign.INCOME -> "+"
            AmountSign.NEUTRAL -> ""
        }
        return prefix + symbol + number
    }
}
