import Foundation
import Testing
@testable import Caffeine

/// Cases mirrored in android-app CurrencyFormatterTest — keep the tables identical.
struct CurrencyFormatterTests {
    let formatter = CurrencyFormatter()

    @Test(arguments: [
        ("6450", AmountSign.expense, "\u{2212}฿6,450"),
        ("52000", AmountSign.income, "+฿52,000"),
        ("1200.5", AmountSign.neutral, "฿1,201"),
        ("0", AmountSign.neutral, "฿0")
    ])
    func whole(raw: String, sign: AmountSign, expected: String) throws {
        let amount = try #require(Decimal(string: raw))
        #expect(formatter.whole(amount, sign: sign) == expected)
    }

    @Test(arguments: [
        ("320", AmountSign.expense, "\u{2212}฿320.00"),
        ("0.005", AmountSign.income, "+฿0.01")
    ])
    func detail(raw: String, sign: AmountSign, expected: String) throws {
        let amount = try #require(Decimal(string: raw))
        #expect(formatter.detail(amount, sign: sign) == expected)
    }
}
