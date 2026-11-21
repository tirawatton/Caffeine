package com.tonapps.caffeine

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.semantics.testTagsAsResourceId
import androidx.compose.ui.tooling.preview.Preview

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent { RootScreen() }
    }
}

/** Placeholder root. Replaced by the tab shell when the first feature runs. */
@OptIn(ExperimentalComposeUiApi::class)
@Composable
fun RootScreen() {
    MaterialTheme {
        Box(
            modifier = Modifier.fillMaxSize().semantics { testTagsAsResourceId = true },
            contentAlignment = Alignment.Center,
        ) {
            Text("Caffeine", style = MaterialTheme.typography.headlineLarge, modifier = Modifier.testTag("root.title"))
        }
    }
}

@Preview
@Composable
private fun RootScreenPreview() = RootScreen()
