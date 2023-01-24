<script lang="ts">
	import { laptops } from '../stores/results';
	import { onMount } from 'svelte';
	import Laptop from './laptop.svelte';
	import { getLaptops } from '../util/search';

	onMount(async () => {
		$laptops = await getLaptops({}, {}, '');
	});
</script>

<main>
	<div>
		{#each $laptops as laptop (laptop.id)}
			{#key laptop.id}
				<Laptop {laptop} />
			{/key}
		{/each}
	</div>
</main>

<style>
	div {
		width: 100%;
		padding: 0.5rem;
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		grid-template-rows: repeat(auto-fit, minmax(250px, 1fr));
		gap: 1rem;
	}

	main {
		width: 100%;
		height: 100%;
		overflow-y: scroll;
	}
</style>
