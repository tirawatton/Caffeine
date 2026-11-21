import Foundation

/// Single THB formatter for the app (see caffeine-domain skill).
/// Android mirror: shared/format/CurrencyFormatter.kt — outputs must match string for string.
enum AmountSign: Sendable { case expense, income, neutral }

struct CurrencyFormatter: Sendable {
    var currencyCode: String = "THB"

    /// Whole baht for lists and heroes, e.g. "−฿6,450" / "+฿52,000" / "฿1,200".
    func whole(_ amount: Decimal, sign: AmountSign) -> String {
        format(amount, fractionDigits: 0, sign: sign)
    }

    /// Two decimals for detail, edit and slip review, e.g. "−฿320.00".
    func detail(_ amount: Decimal, sign: AmountSign) -> String {
        format(amount, fractionDigits: 2, sign: sign)
    }

    private func format(_ amount: Decimal, fractionDigits: Int, sign: AmountSign) -> String {
        var magnitude = amount < 0 ? -amount : amount
        var rounded = Decimal()
        NSDecimalRound(&rounded, &magnitude, fractionDigits, .plain)
        let number = rounded.formatted(
            .number
                .grouping(.automatic)
                .precision(.fractionLength(fractionDigits))
                .locale(Locale(identifier: "en_US"))
        )
        let symbol = currencyCode == "THB" ? "฿" : currencyCode + " "
        let prefix: String = switch sign {
        case .expense: "\u{2212}"
        case .income: "+"
        case .neutral: ""
        }
        return prefix + symbol + number
    }
}
