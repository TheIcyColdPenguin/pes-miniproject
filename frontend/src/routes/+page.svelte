<script lang="ts">
	import AccountArea from '../lib/account-area.svelte';
	import ProductArea from '../lib/product-area.svelte';
	import SearchArea from '../lib/search-area.svelte';
	import Sidebar from '../lib/sidebar.svelte';
</script>

<main>
	<AccountArea />
	<SearchArea />
	<Sidebar />
	<ProductArea />
</main>

<style>
	main {
		width: 100vw;
		height: 100vh;
		margin: 0;
		padding: 0;

		display: grid;
		grid-template-rows: 1fr 10fr;
		grid-template-columns: 2fr 9fr;

		background-color: rgb(232, 219, 240);
	}
</style>
